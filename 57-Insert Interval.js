/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @param {Interval} newInterval
 * @return {Interval[]}
 */
var insert = function(intervals, newInterval) {
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        for(let i = 0;i < intervals.length; i++){
            if(newInterval[0] < i[1]){
                interval[i][0]=newInterval[0]
            }
            if(i[0] > newInterval[0] && i[1] < newInterval[1]){
                intervals.splice(i,1)
            }
            if(newInterval[1] <= i[0] && newInterval[1] < i[1]){
                interval[i][1]=newInterval[1]
            }
        return intervals;
        }