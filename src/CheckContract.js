import { TezosToolkit } from "@taquito/taquito";
import { InMemorySigner } from "@taquito/signer";

async function addIdToContract(contractAddress, newId) {
  const tezos = new TezosToolkit("https://ghostnet.smartpy.io");
  tezos.setProvider({
    signer: await InMemorySigner.fromSecretKey(
      //dont take my tez, this is mainnet ofc 
      "edskS83N9jmmK6yB6G3T58nkTPMVtDaXN4bgLT1kERajL4MtjthUqdcaEYBNyxpHkGPCJ67AwNipykkLtUmH4F6pPxiVhHF1Jk"
    ),
  });
  try {
    const contract = await tezos.contract.at(contractAddress);
    const result = await contract.contractViews.checkId(newId).executeView({
      viewCaller: "KT1PeEYx2XyDZJKvvGDs94GChDwRPdE4bBSz",
    });
    console.log(result);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

// and '5' with the new ID you want to add
addIdToContract("KT1PeEYx2XyDZJKvvGDs94GChDwRPdE4bBSz", 999999);
