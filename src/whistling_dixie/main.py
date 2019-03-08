# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/WhistlingDixie
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


from aqt import mw
from aqt.qt import *
from aqt.reviewer import Reviewer
from anki.hooks import wrap
from .const import *
from .sprezzatura import *


dixie=Dixie()


def wrap_nextCard(reviewer, _old):
    card=dixie.next()
    if card:
        reviewer.cardQueue.append(card)
    return _old(reviewer)


def wrap_answerCard(reviewer, ease, _old):
    if reviewer.mw.state != "review": return
    if reviewer.state != "answer": return
    if dixie.whistle(reviewer.card, ease):
        return reviewer.nextCard() #used to prevent grading card
    return _old(reviewer,ease)


#This could not be wrapped separately due to conflict with other addons.
def wrap_rev_answerButtons(reviewer, _old):
    if not dixie.hasNext(reviewer.card):
        return _old(reviewer)
    buf = """<center><table cellpading=0 cellspacing=0><tr>
<td align=center>%s<button %s title="%s" onclick='py.link("ease%d");'>
%s</button></td></tr></table>"""%(
    'That Was EZ!<br>', "id=defease", _("Shortcut key: %s") % 4, 4, "EZ")
    script = """<script>$(function () { $("#defease").focus(); });</script>"""
    return buf + script


Reviewer.nextCard = wrap(Reviewer.nextCard, wrap_nextCard, 'around')
Reviewer._answerCard = wrap(Reviewer._answerCard, wrap_answerCard, 'around')
Reviewer._answerButtons = wrap(Reviewer._answerButtons, wrap_rev_answerButtons, 'around')



# HOTKEY Setup ============================

def wrap_sched_answerButtons(sched, card, _old):
    if dixie.hasNext(card):
        return 4 #Allows pressing hotkey4 on lrn cards
    return _old(sched, card)

from anki.sched import Scheduler
Scheduler.answerButtons = wrap(Scheduler.answerButtons, wrap_sched_answerButtons, 'around')
if ANKI21:
    import anki.schedv2
    anki.schedv2.Scheduler.answerButtons = wrap(anki.schedv2.Scheduler.answerButtons, wrap_sched_answerButtons, 'around')

