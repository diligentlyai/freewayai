
const { IndexFlatL2, Index, IndexFlatIP, MetricType } = require('faiss-node');

const embeddings = [[
    0.023512473,   -0.06823325,  -0.009247662,    0.002911186,  -0.032679614,
    -0.032778718,    -0.0288641,   0.065111466,    0.005760432,  -0.022125015,
     0.036396023,   -0.02309128,  -0.011601387,   -0.053466722,    0.00956975,
      0.07080996, -0.0061971103,    0.03500856,    0.021332182,   0.019981887,
     0.040459294,  0.0134657845,   0.026634257,    0.035206772,   0.033348568,
    -0.044027045,  -0.030722305,   0.007612442,     0.01612921,   -0.04952733,
    -0.011929669,  -0.036049157,  -0.023128444,     0.02668381,    0.02968171,
     0.011260716,   -0.03961691,   0.014097574,    0.026386496,   0.023041729,
    0.0059586405,  -0.031862002,   0.055399254,      0.0577282,  -0.008801693,
]];

const dem = embeddings[0].length;
const index = new IndexFlatL2(dem);

console.log(index.getDimension());
console.log(index.isTrained());
console.log(index.ntotal());

index.add(embeddings[0]);
// index.add(embeddings[1]);
// index.add(embeddings[2]);
// index.add(embeddings[3]);

console.log(index.ntotal()); // 4