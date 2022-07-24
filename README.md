# Neuron-Reindexer
External tool to fix a problem in the arfificial life game ["The bibites"](https://leocaussan.itch.io/the-bibites)

If you look into JSON file of a Bibite and look at a neuron, you can see it having an attribute called "Index". It would be reasonable to assume, that this is the identifier, which allow the game to know which two neurons are connected by a synapse. This is not the case, though. The games uses the position within the list that stores the neurons as that identifier. It's a purely esthetical attribute that does nothing in the base game. But to Bibite engineers, it can use it to determine that position, without having to count from the top.

But here lies the problem: After a neuron is deleted, all following neurons shift down by one position and the synapses are updated accordingly to point at the correct neurons. But the "Index" attribute doesn't change! It just tells you the wrong index, making it harder to engineer. So...
I made an external tool to fix this problem. 

If Python is not installed on your computer, you're going to have to install it first from [here](https://www.python.org/downloads/).
With  Python installed you just need  to open the neuron-reindexer.pyw file to run the program. It will ask you to select the file you want to be fixed. Select that file. It might not have looked like it, but the tool will have fixed wrong indexes. 
 
