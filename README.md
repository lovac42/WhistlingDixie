# Whistling Dixie: Redo Failed Cards (Positive Reinforcement)


## Usage Scenario no.1:
<img src="https://github.com/lovac42/WhistlingDixie/blob/master/screenshots/smile.png?raw=true">  

If being happy makes us smile, does smiling make us happy? According to psychologist, "Yes we can". What if we apply positive thinking to flashcard reviews? Introducing the one button to RULE them all.  

<img src="https://github.com/lovac42/WhistlingDixie/blob/master/screenshots/ez.png?raw=true">

For every card failed, we force another review, a sort of double dipping where the user could grade again. This phantom review will not be counted or logged, but it will neutralize the negativity received from the previous attempt. By thinking positively, the user becomes more attentive, learns more, and have fun doing so.

<img src="https://github.com/lovac42/WhistlingDixie/blob/master/screenshots/pt.png?raw=true">



## Usage Scenario no.2:
As a child, I often avoid steping on cracks on the sidewalk. Lately, I've developed a general uneasiness towards clicking on the "Again" button similar to the divisions on the sidewalk. When I do click on it, I'll have to go back and redo the grade so that each and every click says "Easy" in my mind.

<img src="https://github.com/lovac42/WhistlingDixie/blob/master/screenshots/crackStepping.png?raw=true">

In this addon, for every failed review, we force a repeat. This is a sort of studied carelessness where every failure is repeated and redone properly. The phantom review will not be counted or logged, but it will neutralize the negativity received from the previous attempt.


## Config:
Due to unknown future compatibility issues, this addon must be manually enabled in the "Study" menu.


## Compatibility Issues:
The phantom card is a copy of the failed review card. As such, it does not exist in the database. But during review, it is treated just the same and triggers the same signals for other addons. However, for addons that automatically edits or reads from this phantom card, they will throw an error. As there are many addons out there, new and old, it is hard to tell which ones will be affected. For that reason, it is the users' responsibility to backup the database and ensure all addons are compatible.

### Anki Fanfare:
This addon works well with Fanfare, but the load order of the addon matter. If Fanfare was loaded first on startup, then this addon cannot trigger the themes to play. Renaming the addon files will cause this addon to be loaded first when anki starts up. On Windows, on the same machine, C drive and D drive will use different load orders, so the prefix used seems to be system/path dependent. Whatever the case, you may need to play around a bit to get things working.

### Warrior Mode:
Requires changing the line with ```...getNote(card.nid)...``` to ```tags=card.note().stringTags()```, simple search and replace.





