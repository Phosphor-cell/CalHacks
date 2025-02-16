/*import fs from "fs/promises";
import path from "path";

const filePath = path.resolve("static/data.json");

export async function POST({ request }){
    try {
        const jsonData = await request.json();

        await fs.writeFile(filePath, JSON.stringify(jsonData, null,2));

        return new Response(JSON.stringify({ message: "Data Saved"}), {
            status: 200,
            headers: {"Content-Type" : "application/json"}
        });
          
    } catch (error) {
        console.error("Error writing file: ", error);
        return new Response(JSON.stringify({error: "Failed to Save"}),{
            status: 500,
            headers: { "Content=Type" : "application/json"}
        });
    }
}*/