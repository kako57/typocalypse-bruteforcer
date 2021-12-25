# typocalypse-bruteforcer
brute forces text for Typocalypse mini-game in Christmas Town in the text-based online game Torn City. Written in Python.

---

## Getting Started
Install the requirements as listed in the file `requirements.txt`
and run `go.py`

```
pip3 install -r requirements.txt
python3 go.py
```

---

### What is this game?

So, I'm playing Torn City, which is a text-based online game.
Every December, there is an event in the game called Christmas Town,
where you can explore Christmas-themed maps for loot. In there, there are also mini-games
that you can play. This year (2021), they added the Typocalypse mini-game where
gifts move along two conveyors. The gifts are tagged with some text. Typing the text
in the input box will make the gift disappear and you get a point.
The gifts are spawned from the topmost conveyor,
then falls on to the next conveyor, then falls down again to some threshold,
which will trigger a loss.

tl;dr it's quite similar to Typer Shark Deluxe.

### Why did you cheat on this mini-game?

I type very slowly. I can only maintain 60 wpm for extended periods of time on English text.
I can only get a maximum of 43 points. So I was kinda sad that there are people reaching 60-120 points
in the mini-game. I thought I can just write a script that will type for me.

### Why this mini-game? Why not cheat on the other ones?

There are helpers that already exist for most of the other mini-games. Typocalypse is a new
mini-game, so there is no helper for it yet. Typocalypse is the first one that actually
requires typing and also is obvious how the score is being derived.

###  Are you even allowed to cheat?

The mini-games give rewards, but they are not based on the outcome. Because of that, this cheat
does not actually give an unfair advantage to other players when it comes to rewards.
This cheat only takes the fun out of the mini-game. It's not like you'll brag about a cheated score, right? Right?

---

## LICENSE

This project is released under the MIT license.
