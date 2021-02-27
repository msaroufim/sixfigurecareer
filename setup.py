import setuptools

# Import github readme as long description
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='sixfigurecareer',  
     version='6.9',
     scripts=['sixfigurecareer'] ,
     author="Mark Saroufim",
     author_email="marksaroufim@gmail.com",
     description="Six figures guaranteed!",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/msaroufim/sixfigurecareer",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT",
         "Operating System :: OS Independent",
     ],
 )