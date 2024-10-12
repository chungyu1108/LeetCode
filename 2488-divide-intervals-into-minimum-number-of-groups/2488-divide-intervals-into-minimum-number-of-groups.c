#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    int* event1 = (int*)a;
    int* event2 = (int*)b;
    if (event1[0] != event2[0])
        return event1[0] - event2[0];
    return event1[1] - event2[1];
}

int minGroups(int** intervals, int intervalsSize, int* intervalsColSize) {
    int n = intervalsSize;
    int events[2 * n][2], eventCount = 0;

    for (int i = 0; i < n; ++i) {
        events[eventCount][0] = intervals[i][0];
        events[eventCount][1] = 1;
        eventCount++;

        events[eventCount][0] = intervals[i][1] + 1;
        events[eventCount][1] = -1;
        eventCount++;
    }

    qsort(events, 2 * n, sizeof(events[0]), compare);

    int max_groups = 0, active_intervals = 0;

    for (int i = 0; i < 2 * n; ++i) {
        active_intervals += events[i][1];
        if (active_intervals > max_groups)
            max_groups = active_intervals;
    }

    return max_groups;
}
