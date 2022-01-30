
# STRAX Race

STRAX Race as the name suggests is a Car racing game, where you can win real STRAX.


## Inspiration
Inspiration
We are a group of unity and python developers. We wanted to integrate both the technologies to come up with something that has real-world usage, and which can be taken forward. So we decided to create a racing car game with a web-based digital wallet using PyStratis.
## Working

It's a racing car game, in which you need to pay small fees of 1 Strax to start the game. To pay the amount you will be directed to the web-based wallet. Once the fee is paid you will be redirected to play the game. Once the game end, if you win you will be credited 2 Strax in the wallet

## How it's made
We have used unity and Stratis Unity SDK to build the car racing game. The game has multiple tracks. We used the Django framework and PyStratis to build the web-based Stratis wallet.
## Installation

Install STRAX Race with git :

```bash
  git clone https://github.com/kampy15/STRAX-Race
```
After completion of cloning run the following commands one by one :
```bash
../> pip install django
../> pip install pystratis
```
Now you have to clone the Stratis Fullnode into your system:
```bash
git clone https://github.com/stratisproject/StratisFullNode.git
git checkout -b release/1.1.1.0
```
Next you have to move at the directory where StraxD is placed,
you can simply do this by the command below:
```bash
../> cd StratisFullNode\src\Stratis.StraxD
```
Now open this file in your Command Prompt and run the next command
```bash
../> dotnet run --env testnet
```
Now leaving this cmd window just like that, move again to the root directory where you cloned STRAX Race initially & open a new command prompt for next command.
```bash
../> python manage.py runserver
