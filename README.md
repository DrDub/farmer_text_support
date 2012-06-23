Farmer Text Support
===================

SMS &lt;-> Recorded Phone Calls Community Knowledge Base

In rural areas cell phones are the only access to technology available. 
This project targets allowing communities to share knowledge through the 
use of SMS and recorded text messages. Moreover, it also allows for 
governmental organizations and NGOs to contribute and track problems in 
the field.

Scenario
--------

A person has a question "Can I plant pineapples alongside mangos?", she 
sends it via SMS to the Farmer Text Support (FTS) server. The FTS then 
either matches the question to an existing question/answer pair on its 
database (using techniques for Information Retrieval on Question/Answer 
archives, an active field of research, see this [http://maroo.cs.umass.edu/pdf/IR-652.pdf] 
paper (Retrieval Models for Question and Answer Archives, PDF) or even 
this [http://www.google.com/patents/US20020169595] patent (Method for 
retrieving answers from an information retrieval system). If no suitable 
recorded answer is found, the question is broadcasted to other subscribers 
via SMS. The subscribers can decide to answer it by calling the FTS and 
leaving a recorded message, which is added to the DB. The original person 
asking the question gets the recorded answer and ranks it.
