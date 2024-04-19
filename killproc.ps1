# Get all processes
$allProcesses = Get-WmiObject Win32_Process

# Loop through each process
foreach ($process in $allProcesses) {
    # Check if the process is blocked (for example, waiting for resources)
    if ($process.ThreadCount -eq 0) {
        Write-Host "Blocked Process: $($process.Name), Process ID: $($process.ProcessId)"
        
        # Get child processes for the blocked process
        $childProcesses = Get-WmiObject Win32_Process | Where-Object { $_.ParentProcessId -eq $process.ProcessId }
        
        # Display child processes
        foreach ($childProcess in $childProcesses) {
            Write-Host "`tChild Process: $($childProcess.Name), Process ID: $($childProcess.ProcessId)"
        }
    }
}
