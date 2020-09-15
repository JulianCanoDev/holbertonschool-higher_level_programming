#!/usr/bin/node
// Print argument
if (Process.argv[2] === undefined)
{
    console.log('No argument');
}
else
{
    console.log(process.argv[2]);
}
