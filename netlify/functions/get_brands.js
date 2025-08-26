
const { Pool } = require('pg');

exports.handler = async function(event, context) {
    const connectionString = process.env.DATABASE_URL;
    if (!connectionString) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Database connection string is not set.' })
        };
    }

    const pool = new Pool({
        connectionString: connectionString,
    });

    try {
        const { rows } = await pool.query('SELECT * FROM brands;');
        return {
            statusCode: 200,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*' // Allow requests from any origin
            },
            body: JSON.stringify(rows)
        };
    } catch (error) {
        console.error('Error fetching brands:', error);
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Failed to fetch brands.' })
        };
    } finally {
        await pool.end();
    }
};
