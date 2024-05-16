

const number_To_string = (value=10000) => {
    // This function is designed to format a number as a string
    // in a format of separation by 3digits
    let to_convert = value.toString()
    let data_length = to_convert.length
    let i = 0
    let converted = ''
    let reversed = ''
    reversed = to_convert.split('').reverse().toString().replaceAll(',','')
    for(i=0; i < data_length; i++){
        if(i%3==0){
            converted =  converted.concat(`.${reversed[i]}`)
        } else {
            converted = converted.concat(`${reversed[i]}`)
        }
    }
    converted = converted.replace('.', '').split('').reverse().toString().replaceAll(',','')
    return converted
}

const data = 10000000
console.log("The formatted version of :", data, 'is: ', number_To_string(data))

