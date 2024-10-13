package hotelbooking;

import hotelbooking.interfaces.*;
import hotelbooking.types.RoomStatus;
import hotelbooking.types.RoomType;

public class Room implements RoomInterface {

    private final String id;
    private final Double price;
    private final RoomType roomType;
    private RoomStatus status;

    public Room(String id, Double price, RoomType roomType) {
        this.id = id;
        this.price = price;
        this.roomType = roomType;
        this.status = RoomStatus.AVAILABLE;
    }

    @Override
    public synchronized void book() {
        try {
            if (this.status == RoomStatus.AVAILABLE) {
                this.status = RoomStatus.BOOKED;
            }
        } catch (Exception e) {
            throw new IllegalStateException("Room is not available for booking.");
        }
    }

    @Override
    public synchronized void checkin() {
        try {
            if (this.status == RoomStatus.BOOKED) {
                this.status = RoomStatus.OCCUPIED;
            }
        } catch (Exception e) {
            throw new IllegalStateException("Room is not booked.");
        }
    }

    @Override
    public synchronized void checkout() {
        try {
            if (this.status == RoomStatus.OCCUPIED) {
                this.status = RoomStatus.AVAILABLE;
            }
        } catch (Exception e) {
            throw new IllegalStateException("Room is not occupied.");
        }
    }

    public String getId() {
        return this.id;
    }

    public Double getPrice() {
        return this.price;
    }

    public RoomStatus getStatus() {
        return this.status;
    }

    public RoomType getRoomType() {
        return this.roomType;
    }

}
