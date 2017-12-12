# MBTA_Network_Analysis
As frequent public transport users, we often find ourselves asking the question of whether our method of transport is efficient. Obviously, using taxi services or driving can be more efficient, but if we are constrained by the use of public transportation, we wonder this constantly. This interdisciplinary project takes on the efficiency problem and maps it to the MBTA. By using an efficiency metric discovered here:

https://www.w3.org/People/Massimo/papers/2001/efficiency_prl_01.pdf

we are able to calculate efficiencies for the MBTA and all of its layers.

First we needed to show that our MBTA network displayed small world phenomenon. By fitting the graph with a power law, we found the slope or gamma, to be greater than 3. This confirmed that our network was in the random regime and that it did in fact, display small world behavior. We could then go forth and calculate efficencies of the network. We found our global efficiency to be approximately 0.67, which is good but not great.

What we hypothesized is that the efficiency of a graph might relate to its robustness. We simulated this by conducting "attacks" on the network. Take for instance that you are an individual who wants to disconnect the T. When destroying robust graphs, you attacks hubs. We attacked graphs based on their efficiencies and found that attacking nodes with the highest efficiencies resulted in similar behavior to attacking nodes with high degree.

What we also noticed was a slight correlation between betweeness centrality and efficency. This makes sense. The nodes with the most shortest graphs going through them, will have the best efficency because their shortest path distances are closer to their euclidean distances to any stop.

Finally we attempted to make the graph more efficient. We used both a random addition and "smart" addition and found that the "smart" addition resulted in higher efficiencies accross the board when we added 10, 50 and 100 paths.

This project was done as a final presentation for PHYS5116 at Northeastern University by Lars Johnsen and Ibrahim Taher. Lars is a BS/MS student in the Industrial Engineering department who is writing his thesis on resilience in networks. Ibrahim is a MS in Data Science candidate.
