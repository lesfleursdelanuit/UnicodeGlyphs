import UnicodeChar from "./UnicodeChar.js";
import runes from "runes";

class UnicodeString{
    constructor(font_manager = null){
        this.symbols = [];
        this.current_id = 0; 
        this.masterset = {};
        this.mapping = [];
        this.cursor = 0; 
        if(font_manager !== null)
            this.font_manager = font_manager; 
    }

    removeSymbol(cursor, value,char_len){
            console.log(char_len);
            this.symbols.splice(cursor,char_len);
            this.cursor = cursor; 
        
    }

    addSymbol(font,style,ch, cursor, value){
            let distinct_chars = runes(ch);
           // console.log("in the unicode model");
           // console.log(distinct_chars);

            for(let i = 0; i < distinct_chars.length; i++){
                this.masterset[this.current_id] = {symbol: new UnicodeChar(distinct_chars[i],font,style,this.current_id), pos: cursor+i};
                this.symbols.splice(cursor+i,0,this.masterset[this.current_id]);
                this.cursor = cursor + i; 
                this.current_id++; 
            }

            console.log("The cursor is: " + this.cursor);
            console.log("The symbols length is: " + this.symbols.length);
            if(this.cursor+1 < this.symbols.length){
                for(let i = this.cursor+1; i < this.symbols.length; i++){
                    console.log("i = " + i);
                    const symbol = this.symbols[i].symbol;
                    const symbol_id = symbol.id; 
                    console.log("symbol id is: " + symbol_id)
                    this.masterset[parseInt(symbol_id)].pos += distinct_chars.length;
                }
            }
        
    }

    makeMapping(){
        let mapping = [];
        for(let i = 0; i < this.symbols.length; i++){
            let symbol = this.symbols[i].symbol;

            for(let j = 0; j < this.font_manager.getGlyph(symbol.font, symbol.style, symbol.char).length; j++)
                mapping.push(symbol.id);
        }

        return mapping; 
    }

    getPositionFromMapping(indexInMapping){
        if(this.symbols.length === 0)
            return -1; 

        console.log("The index in the mapping that we are looking at is: " + indexInMapping);
        let mapping = this.makeMapping();
        console.log(mapping);
        const symbol_id = mapping[indexInMapping];

        return this.masterset[symbol_id].pos; 
    }

    setMapping(){
        this.mapping = this.makeMapping();
    }

    makePlainString(){
        let string = "";
        for(let i = 0; i < this.symbols.length; i++){
            const symbol = this.symbols[i].symbol;
            string += symbol.char; 
        }
        return string; 
    }

    reinstateFromHash(hash){
        let temp = [];
        for(let i = 0; i < hash.symbols.length; i++){
            let symbol_id = hash.symbols[i].id; 
            temp.push(this.masterset[symbol_id]);
        }

        this.cursor = hash.cursor; 
        this.symbols = temp; 
    }

    hashify(){
        let syms = [];
        for(let i = 0; i < this.symbols.length; i++){
            const sym = this.symbols[i].symbol; 
            syms.push(sym.hashify());
        }

        return {cursor: this.cursor, symbols: syms, plainText: this.makePlainString()};
    }

    makeString(){
        let string = "";
        for(let i = 0; i < this.symbols.length; i++){
            const symbol = this.symbols[i].symbol;
            string += this.font_manager.write(symbol.font, symbol.style, symbol.char);
        }
        return string; 
    }
}

export default UnicodeString;