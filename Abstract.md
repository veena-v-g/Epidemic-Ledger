Word count: 261 (Target: 250) 

Blockchain is a type of data structure that involves a chain of blocks that is cryptographically protected with a hash function.  The data within the blocks cannot be altered without all of the blocks being changed leading to an unique transactions.  Blockchain promises anonymity, security, and correctness of the data being stored within these blocks.  

Infectious diseases are caused by pathogenic microorganisms. 
To identify patient zero, we must detect the spread of the disease and find effective treatments, especially at the beginning 
of the outbreak of the infectious disease. Currently, the focus in terms of epidemiological studies has been to prevent the 
outbreak of the diseases.  However, we must understand how to securely, quickly, identify and treat these diseases while 
maintaining the anonymity of the patient, the goal of our project.

The application takes data that has been provided by the user.  The data is provided in the form of CSVs.  The data is then entered into the secured blockchain as key-value pairs (i.e. Key: Location, Value: Buenos Aires).  At the moment, the data cannot be pulled directly from the blockchain into a CSV (Though the pipeline is being developed in a RESTful API and is mocked by the build.gradle files which moves the CSV file into the server), and the data is pulled directly from the secured CSV files and modeled on the website.  Currently, we are using statistical models that are known (i.e. boxplots to determine average location for a set of latitude and longitude points, calculating number of suspected/probable cases) and models the cases on the map.  We used the Zika virus data from the CDC for the dataset for modelling.   
