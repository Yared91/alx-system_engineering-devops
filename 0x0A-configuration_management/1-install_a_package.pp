#!/usr/bin/pup
#install an especific version of flask (2.1.0)
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem'
}
