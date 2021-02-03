# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus. 

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

----------------------------------------------------------------------------------------------------------------------------

Sources:

- Circular Visualization in Python with Piled Ranges. Retrieved from https://stackoverflow.com/questions/62706502/circular-visualization-in-python-with-piled-ranges.

- Dealing with GenBank files in Biopython. Retrieved from https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/genbank.

Libraries I used:
- Matplotlib
- NumPy
- BioPython

Program Notes: 
I used Matplotlib, a Python library, to construct the circular genome map along with NumPy, another Python library. I also utilized BioPython to extract data from the genbank file 
specifically the SeqIO. This module has the functionality that I need to handle the aforesaid file. 

NOTE: To output the circular genome map as a png format, put a path where you want the image to show up on code line 125 of the code. Otherwise, the program will just simply displays the map (but not saving it as png). 
This is something I have not figured out a way to automatically display the map as png without typing its destination path.

