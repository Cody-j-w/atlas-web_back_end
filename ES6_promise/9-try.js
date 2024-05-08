export default function guardrail(mathFunc) {
  const queue = [];

  try {
    queue.push(mathFunc());
  } catch (e) {
    queue.push(e.message);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
