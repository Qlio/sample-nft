const axios = require("axios");
const fs = require("fs");

const main = async () => {
    let continuation;
    do {
        const {
            data: { tokens, continuation: c },
        } = await axios.get("https://api.reservoir.tools/tokens/v6", {
            params: {
                collection: "0xba30e5f9bb24caa003e9f2f0497ad287fdf95623",
                sortBy: "tokenId",
                sortDirection: "asc",
                includeAttributes: true,
                limit: 100,
                continuation: continuation,
            },
        });
        continuation = c;

        for (const { token } of tokens) {
            fs.writeFileSync(
                `./jsons-bakc/${token.tokenId}.json`,
                JSON.stringify({
                    image: `https://raw.githubusercontent.com/Qlio/sample-nft/main/images-bakc/${token.tokenId}.png`,
                    attributes: token.attributes.map(({ key, value }) => ({
                        trait_type: key,
                        value,
                    })),
                })
            );
        }
    } while (continuation);
};

main();
