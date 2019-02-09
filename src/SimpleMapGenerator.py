class SimpleMapGenerator:
    face = 0


"""
class Room extends Sprite {
    // these values hold grid coordinates for each corner of the room
    public var x1:Int;
    public var x2:Int;
    public var y1:Int;
    public var y2:Int;
 
    // width and height of room in terms of grid
    public var w:Int;
    public var h:Int;
 
    // center point of the room
    public var center:Point;
 
    // constructor for creating new rooms
    public function new(x:Int, y:Int, w:Int, h:Int) {
        super();
 
        x1 = x;
        x2 = x + w;
        y1 = y;
        y2 = y + h;
        this.x = x * Main.TILE_WIDTH;
        this.y = y * Main.TILE_HEIGHT;
        this.w = w;
        this.h = h;
        center = new Point(Math.floor((x1 + x2) / 2),
            Math.floor((y1 + y2) / 2));
    }
 
    // return true if this room intersects provided room
    public function intersects(room:Room):Bool {
        return (x1 <= room.x2 && x2 >= room.x1 &&
            y1 <= room.y2 && room.y2 >= room.y1);
    }
}

private function placeRooms() {
    // create array for room storage for easy access
    rooms = new Array();
 
    // randomize values for each room
    for (r in 0...maxRooms) {
        var w = minRoomSize + Std.random(maxRoomSize - minRoomSize + 1);
        var h = minRoomSize + Std.random(maxRoomSize - minRoomSize + 1);
        var x = Std.random(MAP_WIDTH - w - 1) + 1;
        var y = Std.random(MAP_HEIGHT - h - 1) + 1;
 
        // create room with randomized values
        var newRoom = new Room(x, y, w, h);
 
        var failed = false;
        for (otherRoom in rooms) {
            if (newRoom.intersects(otherRoom)) {
                failed = true;
                break;
            }
        }
        if (!failed) {
            // local function to carve out new room
            createRoom(newRoom);
 
            // push new room into rooms array
            rooms.push(newRoom)
        }
    }
}

private function hCorridor(x1:Int, x2:Int, y) {
        for (x in Std.int(Math.min(x1, x2))...Std.int(Math.max(x1, x2)) + 1) {
            // destory the tiles to "carve" out corridor
            map[x][y].parent.removeChild(map[x][y]);
 
            // place a new unblocked tile
            map[x][y] = new Tile(Tile.DARK_GROUND, false, false);
 
            // add tile as a new game object
            addChild(map[x][y]);
 
            // set the location of the tile appropriately
            map[x][y].setLoc(x, y);
        }
    }
 
    // create vertical corridor to connect rooms
    private function vCorridor(y1:Int, y2:Int, x) {
        for (y in Std.int(Math.min(y1, y2))...Std.int(Math.max(y1, y2)) + 1) {
            // destroy the tiles to "carve" out corridor
            map[x][y].parent.removeChild(map[x][y]);
 
            // place a new unblocked tile
            map[x][y] = new Tile(Tile.DARK_GROUND, false, false);
 
            // add tile as a new game object
            addChild(map[x][y]);
 
            // set the location of the tile appropriately
            map[x][y].setLoc(x, y);
        }
    }

    private function placeRooms() {
// store rooms in an array for easy access
rooms = new Array();
 
// variable for tracking center of each room
var newCenter = null;
 
// randomize values for each room
for (r in 0...maxRooms) {
    var w = minRoomSize + Std.random(maxRoomSize - minRoomSize + 1);
    var h = minRoomSize + Std.random(maxRoomSize - minRoomSize + 1);
    var x = Std.random(MAP_WIDTH - w - 1) + 1;
    var y = Std.random(MAP_HEIGHT - h - 1) + 1;
 
    // create room with randomized values
    var newRoom = new Room(x, y, w, h);
 
    var failed = false;
    for (otherRoom in rooms) {
        if (newRoom.intersects(otherRoom)) {
            failed = true;
            break;
        }
    }
    if (!failed) {
        // local function to carve out new room
        createRoom(newRoom);
 
        // store center for new room
        newCenter = newRoom.center;
 
        if(rooms.length != 0){
            // store center of previous room
            var prevCenter = rooms[rooms.length - 1].center;
 
            // carve out corridors between rooms based on centers
            // randomly start with horizontal or vertical corridors
            if (Std.random(2) == 1) {
                hCorridor(Std.int(prevCenter.x), Std.int(newCenter.x),
                    Std.int(prevCenter.y));
                vCorridor(Std.int(prevCenter.y), Std.int(newCenter.y),
                    Std.int(newCenter.x));
            } else {
                vCorridor(Std.int(prevCenter.y), Std.int(newCenter.y),
                    Std.int(prevCenter.x));
                hCorridor(Std.int(prevCenter.x), Std.int(newCenter.x),
                    Std.int(newCenter.y));
                }
            }
        }
    if(!failed) rooms.push(newRoom);
    }
}
"""
