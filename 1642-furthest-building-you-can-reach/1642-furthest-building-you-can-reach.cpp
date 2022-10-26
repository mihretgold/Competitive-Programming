class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
       int r=0,n=heights.size();
        priority_queue<int>q;
        for(r; r<n-1;r++){
            if(heights[r+1]<=heights[r])continue;//if next building < we skip it
            int d=heights[r+1]-heights[r];
            if(d<=bricks){//if the height d/f id >= bricks we use the bricks
                bricks-=d;
                q.push(d);
            }
            else if(ladders >0){//if there are ladders and brick is not enough
               if(q.size()){//if queue is not empty
                   if(q.top()>d){//if the largenum of bricks used > the bricks that would be used now we replace the last brick with a ladder
                       bricks+=q.top();
                       q.pop();
                       q.push(d);
                       bricks-=d;
                   }                  
               }
                 ladders--;
            }
            else break;
        }
        return r;
    }
};