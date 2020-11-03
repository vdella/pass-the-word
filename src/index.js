b64_chosen = () => {
    let phrase = document.getElementById('phrase')
    return document.getElementById("random").is(":checked") ?
        phrase.hidden = false : phrase.hidden = true
}

dict_chosen = () => {
    let slash = document.getElementById('trailing')
    return document.getElementById("dict").is(":checked") ?
        slash.hidden = false : slash.hidden = true
}