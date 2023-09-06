# Reversi_AI

This project will be  composed of 2 parts, one with the python UI and logic and the other with the AI models.

How it will work : 

Environnement will be defined

Agent 1 will be fed state, and pick an action, the logic will give a 2nd state and reward the first agent
Then Agent 2 will be fed state, pick an action and will be rewarded based on 2 things, captures and if he won, if he captures 5 with his action, and agent 1 picks an action that capture 7 he will be rewarded -2
TLDR 
Agent 1 action, Agent 2 action, reward each based on who captured most repeat.

Idea : make it try stuff without rewards for captures.