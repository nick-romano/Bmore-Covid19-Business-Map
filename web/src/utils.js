export const getCapitalLetters = (testString) => {
    const re = RegExp(/\b([A-Z])([a-z]+)?\b/gm);
    const match = testString.match(re);
    let text;
    if (match) {
        text = match.map(r => r[0]).join("")
    } else {
        text = testString;
    }
    return text;
}

