# Ukrainian-OCR

This repo will contain Indian Springs School's custom Ukrainian OCR tool for use in vetting, processing, and aiding refugees fleeing Ukraine. 

## Layout

The following files can be found within the `scripts` directory.

| File Name | Description |
| --- | --- |
| master.py | Contains the full code of the project. Only contains finalized, ready-to-ship versions. |
| image.py | A workspace script for Team A (imaging) to explore methods of reading, processing, and standardizing images. |
| layout-analysis.py | A workspace script for Team B (finding text) to explore methods of document layout analysis and character-finding. |
| character-recognition.py | A workspace script for Team C (pixels-to-data) to explore methods of converting isolated characters into representative data. Note: this script will likely involve a neural network, so please limit access/work to personnel with proper training. |
| processing.py | A workspace script for Team D (processing) to explore methods of handling, storing, vetting, and displaying output data from the OCR software. Note: this script will likely involve GUI and database elements, so please limit access/work to personnel with proper training and authority. |

## Personnel

The following list details personnel names, roles, and descriptions of roles.

| Role | Name | Description |
| --- | --- | --- |
| Project Lead | Andrew Glassford | Person in charge of overseeing deployment, managing relations with contacts, and running project meetings. A legal adult, versed in all related fields of programming and project management. |
| Team Lead: A | Joey Zhu | Person in charge of image processing. Spearheads research of methods to read in, clean up, and orient images. Understands matrices, linear algebra, and related fields of mathematics. |
| Team Lead: B | Catherine Kung | Person in charge of document layout analysis. Responsible for developing code that recognizes characters, words, lines, and related textforms. Note: this particular individual excels in mathematics, allowing for quicker research. |
| Team Lead: C | Henry Spradlin | Person in charge of character recognition. Experienced with and responsible for the creation of AI models capable of converting isolated characters into readable data. Note: this particular individual has a high degree of experience with neural networks, but lacks the mathematical background to fully explain optimization techniques. |
| Team Lead: D | Thomas French | Person in charge of backend data processing. Whatever the AI spits out, this team leader will learn to take it in, display it, store it in databases, and potentially transfer between databases. |