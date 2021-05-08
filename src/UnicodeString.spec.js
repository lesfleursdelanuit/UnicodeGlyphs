import { expect } from 'chai';
 
import UnicodeString from "./UnicodeString.js"; 
import font_manager from "./Glyphs/Font/FontManager.js";
describe('Unicode String', () => {
 let unicode_string = new UnicodeString(font_manager);
  it('Init', () => {
    //let unicode_string = new UnicodeString(font_manager);
    expect(unicode_string.symbols).to.be.eql([]);
    expect(unicode_string.cursor).to.be.eql(0);
    expect(unicode_string.current_id).to.be.eql(0);
    expect(unicode_string.masterset).to.be.eql({});
  });
  it('Insert Character A', () => {
      unicode_string.addSymbol("Fraktur","normal","A",0)
      //console.log(unicode_string);
      expect(unicode_string.cursor).to.be.eql(0);
      expect(unicode_string.current_id).to.be.eql(1);
      expect(unicode_string.symbols.length).to.be.eql(1);
      expect(unicode_string.masterset[0]).to.be.eql(unicode_string.symbols[0]);
      expect(unicode_string.masterset[0].symbol.char).to.be.eql("A");
      expect(unicode_string.masterset[0].symbol.style).to.be.eql("normal");
      expect(unicode_string.masterset[0].symbol.font).to.be.eql("Fraktur");
      expect(unicode_string.masterset[0].symbol.id).to.be.eql(0);
      expect(unicode_string.masterset[0].pos).to.be.eql(0);
  });

  it('Insert Character b after A', () => {
    unicode_string.addSymbol("Fraktur","normal","b",1)
    //console.log(unicode_string);
    expect(unicode_string.cursor).to.be.eql(1);
    expect(unicode_string.current_id).to.be.eql(2);
    expect(unicode_string.symbols.length).to.be.eql(2);
    expect(unicode_string.masterset[1]).to.be.eql(unicode_string.symbols[1]);
    expect(unicode_string.masterset[1].symbol.char).to.be.eql("b");
    expect(unicode_string.masterset[1].symbol.style).to.be.eql("normal");
    expect(unicode_string.masterset[1].symbol.font).to.be.eql("Fraktur");
    expect(unicode_string.masterset[1].symbol.id).to.be.eql(1);
    expect(unicode_string.masterset[1].pos).to.be.eql(1);
    expect(unicode_string.makePlainString()).to.be.eql("Ab");});


    it('Insert Character a "abcd" of characters after b', () => {
        unicode_string.addSymbol("Fraktur","normal","abcd",2);
        //console.log(unicode_string);
        expect(unicode_string.cursor).to.be.eql(5);
        expect(unicode_string.current_id).to.be.eql(6);
        expect(unicode_string.symbols.length).to.be.eql(6);

        const st = "abcd";
        for(let i = 2; i < 6; i++){
            expect(unicode_string.masterset[i]).to.be.eql(unicode_string.symbols[i]);
            expect(unicode_string.symbols[i].symbol.char).to.be.eql(st.charAt(i-2));
        }

        expect(unicode_string.makePlainString()).to.be.eql("Ababcd");});
});