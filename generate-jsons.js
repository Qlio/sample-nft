const axios = require("axios");
const fs = require("fs");

const main = async () => {
    for (let i = 9616; i < 10000; i++) {
        console.log(i);
        const { data } = await axios.get(
            `https://boredapeyachtclub.com/api/mutants/${i}`
        );
        fs.writeFileSync(
            `./jsons-mayc/${i}.json`,
            JSON.stringify({
                image: `https://raw.githubusercontent.com/Qlio/sample-nft/main/images-mayc/${i}.png`,
                attributes: data.attributes,
            })
        );
    }
};

main();
