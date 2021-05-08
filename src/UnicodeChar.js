class UnicodeChar{
    constructor(char, font, style, id){
        // This can be any value in [a-zA-Z0-9]
        this.char = char; 
        // DoubleStruck, Fraktur, Monospace, SansSerif, Script, Serif
        this.font = font; 
        // bold, italic, bold italic, normal
        this.style = style; 
        this.id = id; 

    }
    hashify(){
        return {char: this.char, font: this.font, style: this.style, id: this.id};
    }
}

export default UnicodeChar; 