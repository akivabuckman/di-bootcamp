document.getElementById('lib-button').onclick = generate



function generate(e) {
    e.preventDefault()
    let words = []
    for (let word of document.getElementsByTagName('input')) {
        words.push(word.value)
    }
    for (let i of words) {
        if (i == '') {
            return
        } else {
            continue
        }
    }
    let content = `there was a ${words[0]} that was ${words[1]}, 
        named ${words[2]}. it liked to ${words[3]} in ${words[4]}`;
    document.getElementById('story').textContent = content
}