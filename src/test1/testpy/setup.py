from ament_python.data_files import get_data_files
from ament_python.script_dir import install_scripts_to_libexec
from setuptools import setup

package_name = 'test1_py'
# data_files = get_data_files(package_name)
install_scripts_to_libexec(package_name)

setup(
	name=package_name,
	version='0.0.1',
	packages=[],
	py_modules=[],
		# 'talker'],
	# data_files=data_files,
	install_requires=[
		'setuptools',
		'launch',
		'pyjks'
	],
	author='Vedanth Narayanan',
	author_email='narayave@oregonstate.edu',
	maintainer='Vedanth Narayanan',
	maintainer_email='narayave@oregonstate.edu',
	keywords=['ROS'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python',
		'Topic :: Software Development',
	],
	description='Testing a new python package for ROS2.',
	license='Apache License, Version 2.0',
	test_suite='test',
	entry_points={
		'console_scripts': [
			'talker = talker:main'
		],
	},
)
