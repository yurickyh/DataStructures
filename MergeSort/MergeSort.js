/*------------------------------------------------------------------------
- Execution: node MergeSort.js
- Sort a array of values using merge sort algorithm
- Expected output: 1 2 3 4 5 6
------------------------------------------------------------------------*/
function main(){
    var a = [3,4,2,1,6,5]; //array of values to be sorted
    a = sort(a);
    console.log(a);
}

function sort(array){
    if(array.length == 1){
        return array;
    }
    var merge1 = sort(array.slice(0, array.length/2));
    var merge2 = sort(array.slice(array.length/2, array.length));
    return merge(merge1, merge2);
}

function merge(merge1, merge2){
    var pointer1 = 0; //index for merge1 array
    var pointer2 = 0; //index for merge2 array
    var result = [];
    while(pointer1 < merge1.length || pointer2 < merge2.length){
        if(merge1[pointer1] < merge2[pointer2]){
            result.push(merge1[pointer1]);
            pointer1 += 1;
        }
        else{
            result.push(merge2[pointer2]);
            pointer2 += 1;
        }
        //concat the merge2 array in result array
        if(pointer1 == merge1.length){
            while(pointer2 < merge2.length){
                result.push(merge2[pointer2]);
                pointer2++;
            }
            break;
        }
        //concat the merge1 array in result array
        if(pointer2 == merge2.length){
            while(pointer1 < merge1.length){
                result.push(merge1[pointer1]);
                pointer1++;
            }
            break;
        }
    }
    return result;
}

main()