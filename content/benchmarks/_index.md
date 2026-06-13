---
date: '2025-06-12T12:00:00-07:00'
title: 'Benchmarks — How We Measure Akave Performance'
linkTitle: 'Benchmarks'
description: 'How Akave performance is measured: throughput by workload, TTFB, latency percentiles (P50/P90/P99), and YCSB concurrent benchmarks — plus the latest O3 and network results.'
weight: 7
excludeSearch: true
_build:
  render: always
  list: never
cascade:
  type: docs
---

This section explains **what we test, why it matters, and how to read the numbers**, then publishes the latest measured results for Akave O3 and the Akave Network.

[Akave O3 Results](/benchmarks/o3-results)\
[Akave Network Results](/benchmarks/network-results)

## What we measure

We keep the published set intentionally small so the numbers are easy to compare across runs and over time.

### Throughput by workload (up / down speed)

We measure read (download) and write (upload) throughput across a range of object sizes, from **512 KB** to **512 MB**. Small objects are latency-bound, so per-object overhead dominates and throughput looks low. Large objects are bandwidth-bound and show the ceiling of the connection and storage path. Reporting both ends tells you what to expect for metadata-heavy workloads versus bulk data movement.

### TTFB (Time To First Byte)

TTFB is how long it takes to receive the first byte of a response after a request is sent. It isolates request handling and round-trip latency from raw transfer speed, making it the best single indicator of responsiveness for interactive and streaming workloads.

### Latency percentiles (P50 / P90 / P99)

Averages hide tail behavior. We report:

- **P50** — the median; the typical experience.
- **P90** — 9 out of 10 requests are at least this fast.
- **P99** — the slow tail; what your worst-case users and retries hit.

Tail latency (P99) matters more than the average for production systems, because slow outliers compound under concurrency and retries.

### YCSB concurrent benchmark

[YCSB](https://github.com/brianfrankcooper/YCSB) (Yahoo! Cloud Serving Benchmark) is an industry-standard tool for measuring storage systems under concurrent, mixed workloads. We run it with multiple threads to capture behavior under realistic load:

- **Bulk load** — sustained write throughput while ingesting many objects.
- **Mixed (80% read / 20% write)** — a common production access pattern.

For each phase we report throughput (operations per second) and the P50/P90/P99 latency.

## How to read the results

Numbers reflect a specific test environment (noted on each results page, e.g. a ~10 Gbps connection). Your results will vary with network conditions, region, object size, and concurrency. Use these figures for relative comparison and capacity planning, not as a guarantee.

Results are refreshed regularly as new benchmark runs are published.
