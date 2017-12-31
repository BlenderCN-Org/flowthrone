from __future__ import print_function
import os
import subprocess
from colorama import Fore, Style
import argparse

LIBRARY_PATH = '/usr/local/lib'
INCLUDE_PATH = '/usr/local/include'


def build_and_install_tensorflow(args):
    check_prerequisites(args.tf_repo)
    build(args.tf_repo)
    copy_shared_library(args.tf_repo)
    copy_headers(args.tf_repo)
    copy_third_party(args.tf_repo)


def check_prerequisites(tf_repo_path):
    err_str = ('Provided path should point to a checkout of tensorflow repo, '
               'but does not appear to: {}').format(tf_repo_path)
    if not os.path.exists(tf_repo_path):
        raise Exception(err_str)
    try:
        # Check whether the path is a bazel workspace:
        # 'bazel build' without any arguments will successfully build
        # 0 targets, when executed within a workspace, but will fail otherwise.
        subprocess.check_call(['bazel', 'build'], cwd=tf_repo_path)
    except:
        raise Exception(err_str)


def build(tf_repo_path):
    subprocess.check_call(
        [
            'bazel', 'build', '//tensorflow:libtensorflow_cc.so',
            '//tensorflow:libtensorflow_framework.so'
        ],
        cwd=tf_repo_path)
    print(Fore.GREEN + 'Successfully built tensorflow' + Style.RESET_ALL)


def copy_shared_library(tf_repo_path):
    for cmd in [
        [
            'sudo', 'cp', 'bazel-bin/tensorflow/libtensorflow_cc.so',
            LIBRARY_PATH
        ],
        [
            'sudo', 'cp', 'bazel-bin/tensorflow/libtensorflow_framework.so',
            LIBRARY_PATH
        ],
    ]:
        print(cmd)
        subprocess.check_call(cmd, cwd=tf_repo_path)
    print(Fore.GREEN + 'Successfully copied tensorflow shared library' +
          Style.RESET_ALL)


def copy_headers(tf_repo_path):
    tf_include_path = os.path.join(INCLUDE_PATH, 'google', 'tensorflow')
    cmds = [
        ['sudo', 'mkdir', '-p', tf_include_path],
        ['sudo', 'cp', '--recursive', 'tensorflow', tf_include_path],
    ]
    for cmd in cmds:
        print(cmd)
        subprocess.check_call(cmd, cwd=tf_repo_path)

    subprocess.check_call(
        'sudo find {} -type f ! -name "*.h" -delete'.format(
            os.path.join(tf_include_path, 'tensorflow')),
        shell=True)

    for p in [
            'tensorflow/core/framework',
            'tensorflow/core/kernels',
            'tensorflow/core/lib/core',
            'tensorflow/core/protobuf',
            'tensorflow/core/util',
    ]:
        cmd = 'sudo cp {}/*.h {}/'.format(
            os.path.join(tf_repo_path, 'bazel-genfiles', p),
            os.path.join(tf_include_path, p))
        print(cmd)
        subprocess.check_call(cmd, shell=True)
    print(Fore.GREEN + 'Successfully copied tensorflow headers!' +
          Style.RESET_ALL)


def copy_third_party(tf_repo_path):
    tf_include_path = os.path.join(INCLUDE_PATH, 'google', 'tensorflow')
    for cmd in [['sudo', 'cp', '--recursive', 'third_party', tf_include_path],
                [
                    'sudo', 'rm', '--recursive',
                    os.path.join(tf_include_path, 'third_party/py')
                ]]:
        print(cmd)
        subprocess.check_call(cmd, cwd=tf_repo_path)
    print(Fore.GREEN + 'Successfully copied third_party headers!' +
          Style.RESET_ALL)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=
        '''Helper script for building and installing tensorflow as a shared
           library, to be then used in a CMake project. Prior to running it
           you must first checkout tensorflow repo. The shared library and
           all required headers will be placed in {} and {}, respectively.
           If you decide to modify these paths, make sure to additionally
           modify the FindTensorFlow.cmake to help it find the new location.

           This script is roughly based on the installation steps listed in
           https://github.com/cjweeks/tensorflow-cmake
        '''.format(LIBRARY_PATH, INCLUDE_PATH))
    parser.add_argument('--tf_repo', help='Path to the tensorflow bazel repo')
    args = parser.parse_args()
    if args.tf_repo is None:
        parser.print_help()
    else:
        build_and_install_tensorflow(args)
