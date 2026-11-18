# Java4Shell (CVE-2026-114938): Java runtime security

This repository contains Java source code and **does not supply or configure a
JDK/JRE for your local execution environment**. It cannot patch the JVM
installed on a developer's or user's computer.

If you compile or run this project with an affected OpenJDK HotSpot JVM
(e.g. affected versions of 17, 21, 25, or 27), update to a **vendor-confirmed
fixed JDK/JRE**. Until a fixed vendor build is available, mitigate by setting
`JAVA_TOOL_OPTIONS=-XX:-UseBASE64Intrinsics` before launching Java, javac,
Maven or Gradle, then restart existing JVMs. In PowerShell:
`$env:JAVA_TOOL_OPTIONS = '-XX:-UseBASE64Intrinsics'`.
Check with `java -XX:+PrintFlagsFinal -version` for
`UseBASE64Intrinsics = false`.

Not every Java version or platform is affected: common Java 8/11 JVM
distributions and Android ART do not exercise the described JDK 17+ intrinsic
path. The JDK vendor and CPU features determine practical exposure.

**This is runtime guidance, not an assertion that a vulnerability in this
repository's source code has been patched.**

Sources:
- https://www.cert.europa.eu/publications/security-advisories/2026-021/
- https://adoptium.net/news/2026/11/temurin-november-2026-cspu-java4shell/
