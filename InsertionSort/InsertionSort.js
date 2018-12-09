/*------------------------------------------------------------------------
- Execution: node InsertionSort
- Sort a array of values using insertion sort algorithm
- Expected output: 1 2 3 4 5 6
------------------------------------------------------------------------*/
function main(){
    var v = [3,4,2,1,6,5]; //array of values to be sorted
    insertionSort(v); //exec insertion sort
    console.log(v); //show output
}

function insertionSort(v){
    for(var i = 1; i < v.length; i++){
        const pivot = v[i]; //pivot stores the current value
        var j = i-1;
        for(j = i-1; pivot < v[j] && j >= 0; j--){
            v[j+1] = v[j];
        }
        v[j+1] = pivot; //insert value in the correct position
    }
}

main();