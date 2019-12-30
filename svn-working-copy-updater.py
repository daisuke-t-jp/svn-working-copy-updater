# -*- coding: utf-8 -*-
import sys
import os
import subprocess
import urllib.parse

import config


# functions - svn
def svn_cleanup():
    subprocess.call(['svn', 'cleanup'])

def svn_checkout(url):
    try:
        subprocess.call(['svn', 'checkout', url])
    except:
        raise

def svn_update():
    try:
        subprocess.call(['svn', 'update'])
    except:
        raise


# main
if __name__ == '__main__':
    # Check args.
    args = sys.argv
    if len(args) < 2:
        print('please set working path.')
        sys.exit()
    
    
    # Check working path.
    working_path = args[1]
    if not os.path.exists(working_path):
        print('working path is not exists.')
        sys.exit()
    
    os.chdir(working_path)
    
    
    # Enumerate repositories
    for repo in config.repos():
        url = repo[config.KEY_URL]
        name = repo[config.KEY_NAME]
        
        repo_path = os.path.join(os.getcwd(), name)
        
        try:
            os.makedirs(repo_path)
        except FileExistsError:
            pass
        
        os.chdir(repo_path)
        
        
        # Check .svn directory.
        last_path_component = os.path.basename(os.path.normpath(repo_path))
        working_path2 = os.path.join(os.getcwd(), last_path_component)
        version_path = os.path.join(working_path2, '.svn')
        
        print('repo {0}'.format(url))
        
        if os.path.exists(version_path):
            os.chdir(working_path2)
            
            try:
                svn_update()
            except:
                print("svn clearnup...")
                svn_cleanup()
                svn_update()
        else:
            try:
                svn_checkout(url)
            except:
                print("svn clearnup...")
                svn_cleanup()
                svn_checkout(url)
        

        print('')
        
        os.chdir(working_path)
