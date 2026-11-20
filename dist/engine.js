export function resolveTurn(player, rolls, data) {
  if (player.finished) throw new Error('Hráč už cestu dokončil.');
  if (!Array.isArray(rolls) || !rolls.length || rolls.some(n => !Number.isInteger(n) || n < 1 || n > 6) || rolls.at(-1) === 6 || rolls.slice(0,-1).some(n=>n!==6)) throw new Error('Tah tvoří šestky a jeden závěrečný hod 1–5.');
  const entered = player.position !== null, sixes = rolls.length - 1;
  if (!entered && !sixes) return {position:null,finished:false,path:[],kind:'waiting',amount:0};
  const amount = sixes === 3 ? rolls.at(-1) : rolls.reduce((a,b)=>a+b,0);
  const base = entered ? player.position : (sixes===3 ? 1 : 0);
  const target = base + amount;
  if (target > 72) return {position: entered ? player.position : 6,finished:false,path:[],kind:'overshoot',amount};
  let position=target, path=[target], kind='move';
  const seen = new Set();
  while(data.arrows[position] || data.snakes[position]) {
    if(seen.has(position)) throw new Error('Cyklus v přechodech.'); seen.add(position);
    kind=data.arrows[position]?'arrow':'snake'; position=Number(data.arrows[position] || data.snakes[position]);path.push(position);
  }
  return {position,finished:position===68,path,kind,amount};
}
export function die(random = crypto.getRandomValues.bind(crypto)) {
  const a = new Uint32Array(1); do { random(a); } while(a[0]>=4294967292);
  return a[0]%6+1;
}
export function nextPlayer(players,current) {
  for(let i=1;i<=players.length;i++){let n=(current+i)%players.length;if(!players[n].finished)return n;}
  return -1;
}
export function csvCell(v){const s=String(v??'');return '"'+(/^[=+@\-\t\r]/.test(s)?"'":"")+s.replaceAll('"','""')+'"';}
