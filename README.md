# skill-squatting-attacks-on-amazon-alexa

Amazon allows the development of third-party applications, called “skills”, that leverage Alexa voice services. Up until April of 2017, Alexa required users to enable a skill to their account.
However, Alexa now offers the ability to interact with skills without enabling them.
Skill Squatting Attack: an attacker leverages systematic errors (mis-interpretations) to route a user to malicious application without their knowledge.

Goal of this project: To Analyze alexa’s speech recognition system and find words that the attacker can use for skill creation, such that the probability a user is routed to the malicious skill is highest.

Steps:
Part 1: Alexa Skill Building.

https://developer.amazon.com/en-US/alexa/

Create a skill, set invocation name as "recording obtain" and intent as recording {anything}. The {anything} is search query feature in developer console. You can fing it while creating intents.
The lambda code is in the repositiory. Link your AWS acount with developer console so that you can use AWS services such as dynamo DB. Set endpoints, write lamba functions 

Part 2: Send audio inputs to Alexa skill and collect outputs.

Used NSP dataset for speech samples containing English words spoken by American speakers for analysis of interpretation errors made by Amazon Alexa. 
NSP The Nationwide Speech Project (NSP) is an effort led by Ohio State University to provide structured speech data from a range of speakers across the United States. The NSP corpus provides speech from a total of 60 speakers from six geographical dialect-regions.
For each audio input of NSP sent, we are collecting Alexa’s output  transcription.
Created test-sets for NSP files. Used ASR tool to send input to Alexa. 
ASR allows you to test audio files to measure the accuracy of your skills.
Created scripts to analyze outputs from the JSON file.

Part 3: Accuracy analysis.

-Found words that have UNIQUE MISINTERPRETATIONS
 0% accuracy rate

 Single misinterpretation

 Words found: 64 
 These words can be found from files in the repository.

-Found words that have RANDOM MISINTERPRETATIONS 
 0% accuracy rate

 Multiple misinterpretation

 Words found: 39 
 These words can be found from files in the repository.





