from setuptools import find_packages, setup

heroku ps:scale web=1
setup(
	name='flaskr',
	version='1.0.0',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'flask',
	],
)
