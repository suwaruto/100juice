import tiledmap
import game_master
import dynamic

def main():
    length = 64
    GM = game_master.GameMaster(tiledmap.CircularTileMap(length))
    GM.RegisterCreature(dynamic.Player(0, 0, 10, "player1", []))
    GM.RegisterCreature(dynamic.Player(0, 0, 10, "player2", []))
    i = 1
    while GM.running:
        for player in GM.GetPlayers(): 
            GM.PerformAction(0, player, i)
            print(GM.GetStatus())
        i += 1
            
            
if __name__ == "__main__":
    main()
