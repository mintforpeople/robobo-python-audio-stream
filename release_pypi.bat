pip install twine
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q src\robobopy_audiostream.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*