from fabric.api import env, local, require
from mediachicken import functions


def deploy():
    """fab [environment] deploy"""
    require('environment')
    maintenance_on()
    push()
    build_index()
    maintenance_off()
    ps()


def maintenance_on():
    """fab [environment] maintenance_on"""
    require('environment')
    local('heroku maintenance:on')


def maintenance_off():
    """fab [environment] maintenance_off"""
    require('environment')
    local('heroku maintenance:off')


def push():
    """fab [environment] push"""
    require('environment')
    local('git checkout %s' % env.environment)
    local('git rebase master')
    local('git push --force heroku %s:master' % env.environment)
    local('git checkout master')


def build_index():
    """fab build remote index"""
    local('heroku run python index.py')


def ps():
    """fab [environment] ps"""
    require('environment')
    local('heroku ps')


def open():
    """fab [environment] open"""
    require('environment')
    local('heroku open')



def production():
    """fab production [command]"""
    env.environment = 'deploy'
