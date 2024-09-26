class MyCalendar {
private:
    vector<pair<int, int>> bookings;

public:
    MyCalendar() {}

    bool book(int start, int end) {
        for (const auto& event : bookings) {
            int bookedStart = event.first;
            int bookedEnd = event.second;
            if (start < bookedEnd && bookedStart < end) {
                return false;
            }
        }
        bookings.push_back({start, end});
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */