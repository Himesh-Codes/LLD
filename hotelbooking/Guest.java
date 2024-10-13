package hotelbooking;

public class Guest {

    private final String id;
    private final String name;
    private final String email;
    private final String phone;

    public Guest(String id, String name, String email, String phone) {
        this.phone = phone;
        this.name = name;
        this.id = id;
        this.email = email;
    }

    public String getId() {
        return this.id;
    }

    public String getPhone() {
        return this.phone;
    }

    public String getName() {
        return this.name;
    }

    public String getEmail() {
        return this.email;
    }
}
