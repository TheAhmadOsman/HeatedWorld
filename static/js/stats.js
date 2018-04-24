/* https://stackoverflow.com/questions/48719873/how-to-get-median-and-quartiles-percentiles-of-an-array-in-javascript-or-php */
function Median(data) {
    return Quartile_50(data);
}

function Quartile_25(data) {
    return Quartile(data, 0.25);
}

function Quartile_50(data) {
    return Quartile(data, 0.5);
}

function Quartile_75(data) {
    return Quartile(data, 0.75);
}

function Quartile(data, q) {
    data = Array_Sort_Numbers(data);
    var pos = ((data.length) - 1) * q;
    var base = Math.floor(pos);
    var rest = pos - base;
    if ((data[base + 1] !== undefined)) {
        return data[base] + rest * (data[base + 1] - data[base]);
    } else {
        return data[base];
    }
}

function Array_Sort_Numbers(inputarray) {
    return inputarray.sort(function (a, b) {
        return a - b;
    });
}

function Array_Sum(t) {
    return t.reduce(function (a, b) {
        return a + b;
    }, 0);
}

function Array_Average(data) {
    return Array_Sum(data) / data.length;
}

function Array_Stdev(tab) {
    var i,
        j,
        total = 0,
        mean = 0,
        diffSqredArr = [];
    for (i = 0; i < tab.length; i += 1) {
        total += tab[i];
    }
    mean = total / tab.length;
    for (j = 0; j < tab.length; j += 1) {
        diffSqredArr.push(Math.pow((tab[j] - mean), 2));
    }
    return (Math.sqrt(diffSqredArr.reduce(function (firstEl, nextEl) {
        return firstEl + nextEl;
    }) / tab.length));
}