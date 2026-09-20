import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const html = fs.readFileSync(new URL('../companion/hf_space/index.html', import.meta.url), 'utf8');
const source = html.match(/<script>([\s\S]*?)<\/script>/)[1];
const defaults = {honestyReward:'0.4', lyingCost:'0.2', cooperationBonus:'1', autoRounds:'300', humanRounds:'4', autoRandomness:'.12', humanRandomness:'.12', autoCondition:'reports', humanCondition:'reports'};
const elements = {};
const context = {Math,Number,document:{getElementById(id){
  return elements[id] ??= {value:defaults[id]??'', innerHTML:'',textContent:'',disabled:false, classList:{add(){},remove(){}},addEventListener(){}};
}}};
vm.createContext(context);
vm.runInContext(source,context);
for (const level of ['0.02','0.05','0.12','0.25','0.40']) {
  for (const condition of ['none','reports','market_linked','verified']) {
    context.$('autoCondition').value=condition;
    context.$('autoRandomness').value=level;
    context.runAuto();
    assert.match(context.$('autoResults').innerHTML,/Mutual cooperation/);
    assert.doesNotMatch(context.$('autoResults').innerHTML,/NaN|undefined/);
    context.$('humanCondition').value=condition;
    context.$('humanRandomness').value=level;
    context.startHuman();
    for (const action of ['C','D','C','D']) context.humanPlay(action);
    assert.equal(context.human.round,5);
    assert.equal(context.human.reports,condition==='none'?0:3);
    assert.equal(context.$('humanCooperate').disabled,true);
    assert.doesNotMatch(context.$('humanFinal').innerHTML,/NaN|undefined/);
    context.startHuman();
    assert.equal(context.human.scoreA,0);
    assert.equal(context.human.reporterScore,0);
  }
}
const cfg={honesty:.4,cost:.2,bonus:1};
assert.equal(context.settleReport([0,0],{intrinsic:.4,decision:0},'C','market_linked',cfg),1.4);
assert.equal(context.settleReport([0,0],{intrinsic:.4,decision:0},'D','market_linked',cfg),.4);
assert.equal(context.settleReport([0,0],null,'C','market_linked',cfg),0);
console.log('PASS: 20 agent configurations, 20 complete player games/restarts, delayed bonus checks; no NaN/undefined.');
