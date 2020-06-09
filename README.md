# Normalized Compression Distance and Similarity Metrics
This small project implements a method of malware detection and classification, proving to be efficient and accurate.<br>
Based upon the concept of Normalized Compression Distance (NCD), it measures the similarity between target file and different zoos and further decide which zoo the file belongs to. Therefore, if the zoos are well-established, e.g. one zoo is the set of benign-ware while the other aggregates malware, this method can distinguish whether the file is malicious.<br>
A similarity metric is also generated to visualize the results.<br>
Written in Python.<br>
Supported by `Anaconda`.<br>
## File Description
* similarity_matrix.py: code taking test files and test classes as inputs, calculating the NCD values and generating the similarity metric
* NCD_value.csv: storing all the NCD values between each file and each class
* test_file: files to be detected
* test_class: representing different zoos
* report.pdf: a detailed description of the environment, algorithm, classification results and the similarity metric
## Notes
It is just a simple implementation of the NCD method.<br>
The key factor deciding the accuracy should be the establishment of zoos.