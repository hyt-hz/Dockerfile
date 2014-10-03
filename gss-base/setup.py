from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from distutils.command.install import install as _install

from pkg_resources import Requirement, resource_filename
import os
import shutil
import sys


if '--hep' in sys.argv:
    sys.argv.remove('--hep')
    entry_points = """
        [console_scripts]
        gss_worker_dl = gss.worker.app:dl_main
        gss_controller = gss.controller.app:main
        gss_api = gss.api.gserver:main
        gss_controller_cmd = gss.controller.cmd:start_cmd
        gss_node = gss.api.cli:gss_node
        gss_hep = gss.hep.api.client:gss_hep_cli
        gss_downloader = gss.common.downloader:main
        gss_debug_worker = gss.worker.cli:main
        gss_debug_controller = gss.controller.cli:main
    """
else:
    entry_points = """
        [console_scripts]
        gss_worker_file = gss.worker.app:file_main
        gss_worker_dl = gss.worker.app:dl_main
        gss_controller = gss.controller.app:main
        gss_api = gss.api.gserver:main
        gss_controller_cmd = gss.controller.cmd:start_cmd
        gss_cli = gss.api.cli:gss_obj
        gss_node = gss.api.cli:gss_node
        gss_cms = gss.api.cli:gss_cms
        gss_downloader = gss.common.downloader:main
        gss_debug_worker = gss.worker.cli:main
        gss_debug_controller = gss.controller.cli:main
    """



#here = os.path.abspath(os.path.dirname(__file__))
#README = open(os.path.join(here, 'README.md')).read()
#CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

PKG_NAME = 'gss'

# to make sure lxml can be properly installed,
# yum install libxml2-dev
# yum install libxslt-devel

requires = [
    'python-daemon',
    'requests',
    'gevent',
    'Flask',
    'gunicorn',
    'PyYAML',
    'pymongo',
    'docopt',
    'lxml',
    'ipaddress',
    'redis>=2.10',
    'psutil'
]

test_requires = [
    'unittest2'
]


def copy_no_overwrite(src, dst):
    names = os.listdir(src)

    if not os.path.exists(dst):
        os.makedirs(dst)
    errors = []
    for name in names:
        src_name = os.path.join(src, name)
        dst_name = os.path.join(dst, name)
        try:
            if os.path.isdir(src_name):
                copy_no_overwrite(src_name, dst_name)
            elif not os.path.exists(dst_name):
                shutil.copy2(src_name, dst_name)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except shutil.Error, err:
            errors.extend(err.args[0])
        except EnvironmentError, why:
            errors.append((src_name, dst_name, str(why)))
    try:
        shutil.copystat(src, dst)
    except OSError, why:
        if WindowsError is not None and isinstance(why, WindowsError):
            # Copying file access times may fail on Windows
            pass
        else:
            errors.append((src, dst, str(why)))
    if errors:
        raise shutil.Error, errors


def copy_conf_file():
    print 'copy config file successfully'
    #filename = resource_filename(Requirement.parse(PKG_NAME), "etc")
    filename = os.path.join(here, 'etc')
    copy_no_overwrite(filename, '/etc')


class MyInstall(install):
    def run(self):
        ### some dirty hack
        ret = None
        # Explicit request for old-style install?  Just do it
        if self.old_and_unmanageable or self.single_version_externally_managed:
            ret = _install.run(self)
        else:
            # Attempt to detect whether we were called from setup() or by another
            # command.  If we were called by setup(), our caller will be the
            # 'run_command' method in 'distutils.dist', and *its* caller will be
            # the 'run_commands' method.  If we were called any other way, our
            # immediate caller *might* be 'run_command', but it won't have been
            # called by 'run_commands'.  This is slightly kludgy, but seems to
            # work.
            #
            caller = sys._getframe(2)
            caller_module = caller.f_globals.get('__name__','')
            caller_name = caller.f_code.co_name

            if caller_module != 'distutils.dist' or caller_name!='run_commands':
                # We weren't called from the command line or setup(), so we
                # should run in backward-compatibility mode to support bdist_*
                # commands.
                _install.run(self)
            else:
                self.do_egg_install()
        #copy_conf_file()
        return ret


class MyDevelop(develop):
    def run(self):
        develop.run(self)
        copy_conf_file()


setup(
    name=PKG_NAME,
    version='0.1',
    description='Gensee Storage System',
    #long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python"
    ],
    author='',
    author_email='',
    url='',
    keywords='gss storage REST',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    #cmdclass = {'install': MyInstall,
    #            'develop': MyDevelop},
    tests_require=requires + test_requires,
    test_suite="gss.unit_test",
    entry_points=entry_points
    )

